import requests
import concurrent.futures
from termcolor import colored
from tqdm import tqdm
import urllib3

#check do dominio para ver se está 200
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def check_domain(domain, out_file, timeout=2):
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(f"https://{domain}", timeout=timeout,verify=False)
        if response.status_code == 200:
            out_file.write(f"https://{domain}\n")
    except requests.exceptions.RequestException as e:
        try:
            response = session.get(f"http://{domain}", timeout=timeout,verify=False)
            if response.status_code == 200:
                out_file.write(f"http://{domain}\n")
        except requests.exceptions.RequestException as e:
            pass

def test_domains(file_in, file_out):
    with open(file_in, 'r') as in_file:
        with open(file_out, 'w') as out_file:
            domains = [line.strip() for line in in_file]
            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                futures = [executor.submit(check_domain, domain, out_file) for domain in domains]
                for _ in tqdm(concurrent.futures.as_completed(futures), total=len(domains)):
                    pass

