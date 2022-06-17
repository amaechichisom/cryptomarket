# %%
import pandas as pd
import os
from cryptospiders import Crawlers
os.chdir("C:\\Users\\USER\\Documents\\Python-Jobs\\Eden-AI\\cryptomarket")

# %%
# obj = Crawlers().coinbureau()

# if obj is not None:
#     with open(obj[0], 'w', encoding='utf-8') as file:
#         file.write(obj[1])
#         file.close()
#     print('\nProcessing complete')

# %%


def convert_json_to_csv(site):
    with open(site+'.json', encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
        
    df.to_csv(site+'.csv', encoding='utf-8', index=False)

# site = int(input("Select a website to crawl:\tCoinbureau(1) Forbes(2) Moneyweb(3)\n>>> "))


# obj = eval('Crawlers().forbes()')

# if obj is not None:
#     with open('forbes'+'.json', 'w', encoding='utf-8') as file:
#         file.write(obj[1])
#         file.close()
#     convert_json_to_csv('forbes')
#     print('\nProcessing complete')

for site in [1,2,3]:
    print("hello i ran")
    from cryptospiders import Crawlers
    sites = {1:'coinbureau', 2:'forbes', 3:'moneyweb'}
    obj = eval('Crawlers().' + str(sites.get(site)) + '()')

    if obj is not None:
        with open(sites.get(site)+'.json', 'w', encoding='utf-8') as file:
            file.write(obj[1])
            file.close()
        convert_json_to_csv(sites.get(site))
        print('\nProcessing complete')
# else:
#     print("Not a valid choice")



