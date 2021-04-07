# JustMecha



#### Idea behind this project

I'm a big fan of GUNDAM mechas. But I easily get tired while looking for the best price for a specific model. So, I decided to build a simple CLI application to find the best offer.

I usually buy models in two polish shop: [Zinch Mecha](https://www.zincmecha.com) and [Mirage Shop](https://www.mhshop.pl). That's why I only search through these shops.

##### Used packages

1. **Python v. 3.9**
2. **BeautifulSoup v. 4.9.3**
3. **Datetime v. 4.3**
4. **Pandas v. 1.2.3**
5. **Click v. 7.1.2**
6. **Colorama v. 0.4.4**

#### How to use it?

1. Download or clone repository
2. In root folder type in console `py main.py --mecha-name --mecha-scale` (example: `py main.py "aile strike" MG`)
3. Type `py main.py --help` to print help.

Output should look like this:

````
                                 Mecha   Price        Seen Scale    Shop
0  MG 1/100 AILE STRIKE GUNDAM VER. RM  229.95  07-04-2021    MG   zinch
1          GUNDAM MG 81349 AILE STRIKE  239.00  07-04-2021    MG  mirage
"Lowest price is 229.95. Scale: ['MG']. Can be found in ['zinch']"
````



