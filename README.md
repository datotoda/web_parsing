# Store Edision Web Scraping

main.py პროგრამის გაშვებისას ტერმინალში გამოდის დიალოგური რეჟიმი, 
სადაც შეგიძლიათ აირჩიოთ შემოთავაზებული კატეგორიებიდან ერთ-ერთი და წამოიღოთ მონაცემები 
[store.edison.ge](https://store.edison.ge/) საიტიდან. დაწერეთ კატეგორიის სრული სახელი. 
შემდეგ პროგრამა შეგეკითხებათ გვერდების რაოდენობას და საბოლოოდ მოძიებულ ინფორმაციას შეინახავს database.csv ფაილში. 
ასევე პროგრამა დაგიწერთ სავარაუდო მოცდის დროსა და თითოეული გვერდისთვის საჭირო დროს.

---

## საჭირო მოდულების ინსტალაცია

``$ pip install -r requirements.txt``

## გამოყენების მაგალითი


``$ python main.py``

```
Choose one:
        modules and sensors  
        electronic components
        chargers
        chips
        tools
```

``> tools``

```
How many pages do you want? (1 to 12): 
```

``> 2``

```
Estimated sleep time: 9.45 s
Page N-1 parsed in 0.64 s
Start sleep
End sleep in 8.44
Page N-2 parsed in 0.53 s
----------------------------------------
Successfully completed in 9.61 seconds
```



