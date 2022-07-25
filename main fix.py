import requests 
from bs4 import BeautifulSoup 
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time 
import pandas as pd 

for page in range(0,61):
    if page==0:
        webpage = input("Enter your url : ")
        #webpage = input("Enter url tripadvisor: ")      


        driver = webdriver.Chrome(ChromeDriverManager().install())
        try:
            driver.get(webpage)
        except:
            driver.get(webpage)

                #sbox = driver.find_element_by_xpath('//*[@id="txtSearch"]')
                #sbox.send_keys(searchterm)

                #submit = driver.find_element_by_xpath('//*[@id="btnSearchResult"]')
                #submit.click()
        current_url = driver.current_url


                # Driver scrolls down three times to load the table.
        for i in range(0,3):
            driver.execute_script("window.scrollBy(0,5000)")
            time.sleep(2)
                # print(driver.page_source)  # results


        soup = BeautifulSoup(driver.page_source,'html.parser')
        # print(soup.prettify())

        title= [ i.text for i in soup.find_all('span',{'class':'noQuotes'})]
        print(title)
        print(len(title))

        comment = [i.text for i in soup.find_all('p',{'class':'partial_entry'})]
        print(comment)
        print(len(comment))

        username = [ i.text for i in soup.find_all('div',{'class':'info_text pointer_cursor'})] 
        print(username)
        print(len(username))

        date_visit = [i.text.replace('Date of visit:','').strip() for i in soup.find_all('div',{'class':'prw_rup prw_reviews_stay_date_hsx'})]
        print(date_visit)
        print(len(date_visit))

        review = [] #contributed
        for i in soup.find_all('div',{'class':'member_info'}):
            print(i)
            if i.find('div',{'class':'reviewerBadge badge'}):
                review.append(i.find('div',{'class':'reviewerBadge badge'}).text.replace('reviews','').strip())
            else: 
                review.append('0')

        print(review)
        print(len(review))





        mobile = []
        for i in soup.find_all('div',{'class':'ui_column is-9'}):
            if i.find('span',{'class':'viaMobile'}):
                mobile.append('1')
            else: 
                mobile.append('0')
        print(mobile)
        print(len(mobile))

        writing_date = [ i.text.replace('Reviewed','').strip() for i in soup.find_all('span',{'class':'ratingDate'})]
        print(writing_date)
        print(len(writing_date))

        rating = []
        for i in soup.find_all('div',{'class':'ui_column is-9'}): 
            tes = i.find('span',{'class':'ui_bubble_rating'})
            print(tes)
            try:
                if i.find('span',{'class':'ui_bubble_rating bubble_50'}):
                    rating.append("5")
                elif i.find('span',{'class':'ui_bubble_rating bubble_40'}):
                    rating.append("4")
                elif i.find('span',{'class':'ui_bubble_rating bubble_30'}):
                    rating.append("3")
                elif i.find('span',{'class':'ui_bubble_rating bubble_20'}):
                    rating.append("2")
                elif i.find('span',{'class':'ui_bubble_rating bubble_10'}):
                    rating.append("1")
                else:
                    rating.append("0")
            except:
                pass

        rating = rating[:len(title)]
        print(rating)


        
        #loc = []
        #div_loc = soup.find_all('div',{'class':'userLoc'})
        #if len(div_loc) > 0: 
        #    for i in div_loc:
        #        loc.append(i)
        #else:
        #    loc = [ soup.find('span',{'class':'yEWoV OkcwQ'}).text for i in range(len(title)) ]
                
        #print(loc,len(loc))

  
        comment_number = len(username)
        
        df = pd.DataFrame()

        df['profile'] = [ 'https://www.tripadvisor.com/Profile/{}'.format(i) for i in username][:comment_number]
        df['url'] = [ webpage for i in range(len(username))][:comment_number]
        df['title'] = title[:comment_number]
        df['text'] = comment[:comment_number]
        df['username'] = username[:comment_number]
        df['rating'] = rating[:comment_number]
        # df['location'] = loc
        df['contributed'] = review[:comment_number]
        df['date'] = writing_date[:comment_number]
        df['experience'] = date_visit[:comment_number]
        df['mobile'] = mobile[:comment_number]


        df.to_excel("scrape{}.xlsx".format(page))
    else:

        webpage = "https://www.tripadvisor.com/Restaurant_Review-g1215781-d7690429-Reviews-or{}-Go_Benz_Phuket-Phuket_Town_Phuket.html".format(page) # edit me
        #webpage = input("Enter url tripadvisor: ")      


        driver = webdriver.Chrome(ChromeDriverManager().install())
        try:
            driver.get(webpage)
        except:
            driver.get(webpage)

                #sbox = driver.find_element_by_xpath('//*[@id="txtSearch"]')
                #sbox.send_keys(searchterm)

                #submit = driver.find_element_by_xpath('//*[@id="btnSearchResult"]')
                #submit.click()
        current_url = driver.current_url


                # Driver scrolls down three times to load the table.
        for i in range(0,3):
            driver.execute_script("window.scrollBy(0,5000)")
            time.sleep(2)
                # print(driver.page_source)  # results


        soup = BeautifulSoup(driver.page_source,'html.parser')
        # print(soup.prettify())

        title= [ i.text for i in soup.find_all('span',{'class':'noQuotes'})]
        print(title)
        print(len(title))

        comment = [i.text for i in soup.find_all('p',{'class':'partial_entry'})]
        print(comment)
        print(len(comment))

        username = [ i.text for i in soup.find_all('div',{'class':'info_text pointer_cursor'})] 
        print(username)
        print(len(username))

        date_visit = [i.text.replace('Date of visit:','').strip() for i in soup.find_all('div',{'class':'prw_rup prw_reviews_stay_date_hsx'})]
        print(date_visit)
        print(len(date_visit))

        review = [] #contributed
        for i in soup.find_all('div',{'class':'member_info'}):
            print(i)
            if i.find('div',{'class':'reviewerBadge badge'}):
                review.append(i.find('div',{'class':'reviewerBadge badge'}).text.replace('reviews','').strip())
            else: 
                review.append('0')

        print(review)
        print(len(review))





        mobile = []
        for i in soup.find_all('div',{'class':'ui_column is-9'}):
            if i.find('span',{'class':'viaMobile'}):
                mobile.append('1')
            else: 
                mobile.append('0')
        print(mobile)
        print(len(mobile))

        writing_date = [ i.text.replace('Reviewed','').strip() for i in soup.find_all('span',{'class':'ratingDate'})]
        print(writing_date)
        print(len(writing_date))

        rating = []
        for i in soup.find_all('div',{'class':'ui_column is-9'}): 
            tes = i.find('span',{'class':'ui_bubble_rating'})
            print(tes)
            try:
                if i.find('span',{'class':'ui_bubble_rating bubble_50'}):
                    rating.append("5")
                elif i.find('span',{'class':'ui_bubble_rating bubble_40'}):
                    rating.append("4")
                elif i.find('span',{'class':'ui_bubble_rating bubble_30'}):
                    rating.append("3")
                elif i.find('span',{'class':'ui_bubble_rating bubble_20'}):
                    rating.append("2")
                elif i.find('span',{'class':'ui_bubble_rating bubble_10'}):
                    rating.append("1")
                else:
                    rating.append("0")
            except:
                pass

        rating = rating[:len(title)]
        print(rating)

        #loc = []
        #div_loc = soup.find_all('div',{'class':'userLoc'})
        #if len(div_loc) > 0: 
        #    for i in div_loc:
        #        loc.append(i)
        #else:
        #    loc = [ soup.find('span',{'class':'yEWoV OkcwQ'}).text for i in range(len(title)) ]
                
        #print(loc,len(loc))


        df = pd.DataFrame()
        comment_number = len(username)
        
        

        df['profile'] = [ 'https://www.tripadvisor.com/Profile/{}'.format(i) for i in username][:comment_number]
        df['url'] = [ webpage for i in range(len(username))][:comment_number]
        df['title'] = title[:comment_number]
        df['text'] = comment[:comment_number]
        df['username'] = username[:comment_number]
        df['rating'] = rating[:comment_number]
        # df['location'] = loc
        df['contributed'] = review[:comment_number]
        df['date'] = writing_date[:comment_number]
        df['experience'] = date_visit[:comment_number]
        df['mobile'] = mobile[:comment_number]

        df.to_excel("scrape{}.xlsx".format(page))


#rating = [ i for i in soup.find_all('div',{'class':'memberBadgingNoText is-shown-at-tablet'})]
#print(rating)
#print(len(rating))


