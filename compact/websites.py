class cardekho:
    sel='//ul[@id="content"]/li'
    city='div[1]/div[3]/div[2]/div[2]/span[1]/text()'
    yom='div[1]/div[2]/div[3]/ul/li[2]/div[2]/span/text()'
    price='div[1]/div[3]/div[1]/text()'
    kms='div[1]/div[2]/div[3]/ul/li[1]/div[2]/span/text()'
    transm='div[1]/div[2]/div[3]/ul/li[4]/div[2]/text()'
    fuel='div[1]/div[2]/div[3]/ul/li[3]/div[2]/text()'
    model='div[1]/div[2]/div[1]/a/text()'
    owner='div[1]/div[2]/div[3]/ul/li[5]/div[2]/text()'
    url='div[1]/div[2]/div[1]/a/@href'
    url1='http://www.cardekho.com/used-cars+in+delhi-ncr'
    url2="http://www.cardekho.com/used-cars+in+delhi-ncr/%d"
    color='div[1]/div[2]/div[2]/div[2]/text()'

class gaadi:
    sel='//ul[@class="clearfix list-unstyled usdcartable"]/li'
    model='article/div[2]/h2/a/text()'
    price='article/div[2]/div/div[2]/p[1]/text()'
    kms='article/div[2]/div/div[1]/div[1]/div[1]/ul/li[1]/div/text()'
    fuel='article/div[2]/div/div[1]/div[1]/div[1]/ul/li[3]/div/text()'
    yom='article/div[2]/div/div[1]/div[1]/div[1]/ul/li[2]/div/text()'
    city='article/div[2]/div/div[1]/p[2]/text()'
    url='article/div[2]/h2/a/@href'
    transm='article/div[2]/div/div[1]/div[1]/div[1]/ul/li[3]/div/text()'
    owner='//body[not(node())]'
    url1='http://www.gaadi.com/filter/used_car_result.php?city='
    url2="http://www.gaadi.com/filter/used_car_result.php?city=&pg=%d"
    color='article/div[2]/div/div[1]/div[1]/div[1]/ul/li[4]/div/text()'

class cartrade:
    sel='//div[@class="btmMrg carlistblk"]'
    model='div/div[2]/div[2]/div[1]/div[1]/a/text()'
    price='div/div[2]/div[2]/div[1]/div[5]/div[1]/strong/text()'
    kms='div/div[2]/div[2]/div[3]/table/tr[1]/td[2]/label/text()'
    fuel='div/div[2]/div[2]/div[3]/table/tr[1]/td[1]/label/text()'
    transm='div/div[2]/div[2]/div[3]/table/tr[2]/td[2]/label/text()'
    city='div/div[2]/div[2]/div[3]/table/tr[3]/td[2]/label/text()'
    yom='//body[not(node())]'
    owner='div/div[2]/div[2]/div[3]/table/tr[2]/td[1]/label/text()'
    url='div/div[2]/div[2]/div[1]/div[1]/a/@href'
    url1='http://www.cartrade.com/buy-used-cars'
    url2="http://www.cartrade.com/buy-used-cars/p-%d"
    color='div/div[2]/div[2]/div[3]/table/tr[3]/td[1]/label/text()'
