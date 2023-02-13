import requests
import concurrent.futures
from termcolor import colored
from tqdm import tqdm
import argparse
import tempfile
import urllib3




urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#check hosts up
#passar dominio ou arquivo de dominios e qual arquivo escrever
def check_domain(domain, out_file, timeout=2):
    if not domain.startswith("http"):
        domain = "https://" + domain
    
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=3)
    session.mount('https://', adapter)
    session.mount('http://', adapter)

    try:
        response = session.get(domain, timeout=timeout,verify=False)
        if response.status_code == 200:
            out_file.write(domain + "\n")
    except requests.exceptions.RequestException as e:
        if domain.startswith("https://"):
            domain = domain.replace("https://", "http://")
            try:
                response = session.get(domain, timeout=timeout,verify=False)
                if response.status_code == 200:
                    out_file.write(domain + "\n")
            except requests.exceptions.RequestException as e:
                pass

def test_domains(file_in, file_out,valor):
    with open(file_in, 'r') as in_file:
        with open(file_out, 'w') as out_file:
            domains = [line.strip() for line in in_file]
            with concurrent.futures.ThreadPoolExecutor(max_workers=valor) as executor:
                futures = [executor.submit(check_domain, domain, out_file) for domain in domains]
                for _ in tqdm(concurrent.futures.as_completed(futures), total=len(domains)):
                    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Verifique um domínio ou uma lista de domínios e grave os disponíveis em um arquivo de saída.')
    parser.add_argument('input', help='Arquivo de entrada com a lista de domínios ou um único domínio.')
    parser.add_argument('-o', help='Nome do arquivo de saida, default= hosts-200.txt')
    parser.add_argument('-t', type=int, default=100, help='passe o numero de threads a ser executado, default = 100')
    args = parser.parse_args()
    try:
        with open(args.input, 'r') as in_file:
            pass
    except FileNotFoundError:
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp:
            temp.write(args.input + "\n")
            args.input = temp.name
    if not args.o:
        with open(args.input, 'r') as in_file:
            first_domain = in_file.readline().strip()
            args.o = first_domain + ".txt"
    test_domains(args.input, args.o,args.t)


