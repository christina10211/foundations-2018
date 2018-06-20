
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


response = requests.get('https://techcrunch.com/')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


#I figured that the feature posts are not available without javascript, 
#so I scrape the stories under 'The Latest' part.
#print(response.text)


# In[4]:


list_of_stories = []

articles = doc.find_all(class_ = 'post-block')
for article in articles:
    story_dict = {}
    headline = article.find(class_ = 'post-block__title')
    
    author = article.find(class_ = 'river-byline__authors')
    summary = article.find(class_ = "post-block__content")
    
    url = article.find('a')['href']
    if headline:
        story_dict['Headline'] = headline.text.strip()
    if author:
        story_dict['Author'] = author.text.strip()
    if summary:
        story_dict['Summary'] = summary.text.strip()
    if url:
        story_dict['url'] = url
    list_of_stories.append(story_dict)
    
#list_of_stories



# In[5]:


pd.set_option('display.max_colwidth', -1)
df = pd.DataFrame(list_of_stories)
df.head()


# In[6]:


import datetime

right_now = datetime.datetime.now()
right_now


# In[7]:


# http://strftime.org/ 


# In[8]:


time_string = right_now.strftime("%Y-%m-%d-%-I%p")
time_string
hour_string = right_now.strftime("%-I%p")
hour_string


# In[9]:


filename = "briefing-" + time_string + ".csv"
filename


# In[10]:


df.to_csv(filename, index=False)


# In[11]:


stories_string = str(list_of_stories)


# In[12]:


"Thie is your "+hour_string+" TechCrunch briefing "


# In[13]:


emailbody = df.to_html()



# In[14]:


response = requests.post(
        "https://api.mailgun.net/v3/sandbox069bc2aaa4974001b7b17a41ecef39d0.mailgun.org/messages",
        auth=("api", "YOUR API KEY"),
        files=[("attachment", open(filename))],
        data={"from": "Little Little <mailgun@sandbox069bc2aaa4974001b7b17a41ecef39d0.mailgun.org>",
              "to": ["zz2564@columbia.edu"],
              "subject": "Thie is your "+hour_string+" TechCrunch briefing ",
              "html": "<html>"+emailbody+"</html>",
              "text": stories_string})
            
response.text

