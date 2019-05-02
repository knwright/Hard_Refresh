#!/usr/bin/env python
# coding: utf-8

# In[16]:



from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

urls = [
    'http://www.espn.com/nhl/team/roster/_/name/chi/chicago-blackhawks',
    'http://www.espn.com/nhl/team/roster/_/name/col/colorado-avalanche',
    'http://www.espn.com/nhl/team/roster/_/name/dal/dallas-stars',
    'http://www.espn.com/nhl/team/roster/_/name/min/minnesota-wild',
    'http://www.espn.com/nhl/team/roster/_/name/nsh/nashville-predators',
    'http://www.espn.com/nhl/team/roster/_/name/stl/st-louis-blues',
    'http://www.espn.com/nhl/team/roster/_/name/wpg/winnipeg-jets',
    'http://www.espn.com/nhl/team/roster/_/name/ana/anaheim-ducks',
    'http://www.espn.com/nhl/team/roster/_/name/ari/arizona-coyotes',
    'http://www.espn.com/nhl/team/roster/_/name/cgy/calgary-flames',
    'http://www.espn.com/nhl/team/roster/_/name/edm/edmonton-oilers',
    'http://www.espn.com/nhl/team/roster/_/name/la/los-angeles-kings',
    'http://www.espn.com/nhl/team/roster/_/name/sj/san-jose-sharks',
    'http://www.espn.com/nhl/team/roster/_/name/van/vancouver-canucks',
    'http://www.espn.com/nhl/team/roster/_/name/vgs/vegas-golden-knights',
    'http://www.espn.com/nhl/team/roster/_/name/bos/boston-bruins',
    'http://www.espn.com/nhl/team/roster/_/name/buf/buffalo-sabres',
    'http://www.espn.com/nhl/team/roster/_/name/det/detroit-red-wings',
    'http://www.espn.com/nhl/team/roster/_/name/fla/florida-panthers',
    'http://www.espn.com/nhl/team/roster/_/name/mtl/montreal-canadiens',
    'http://www.espn.com/nhl/team/roster/_/name/ott/ottawa-senators',
    'http://www.espn.com/nhl/team/roster/_/name/tb/tampa-bay-lightning',
    'http://www.espn.com/nhl/team/roster/_/name/tor/toronto-maple-leafs',
    'http://www.espn.com/nhl/team/roster/_/name/car/carolina-hurricanes',
    'http://www.espn.com/nhl/team/roster/_/name/cbj/columbus-blue-jackets',
    'http://www.espn.com/nhl/team/roster/_/name/nj/new-jersey-devils',
    'http://www.espn.com/nhl/team/roster/_/name/nyi/new-york-islanders',
    'http://www.espn.com/nhl/team/roster/_/name/nyr/new-york-rangers',
    'http://www.espn.com/nhl/team/roster/_/name/phi/philadelphia-flyers',
    'http://www.espn.com/nhl/team/roster/_/name/pit/pittsburgh-penguins',
    'http://www.espn.com/nhl/team/roster/_/name/wsh/washington-capitals'
    ]



options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)

for url in urls:

    driver.get(url)

    images = driver.find_elements_by_tag_name('img')
    for image in images:
        print(image.get_attribute('src'))

    
    


# In[ ]:


driver.close()

