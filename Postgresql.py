
# coding: utf-8

# In[25]:


import psycopg2


# In[26]:


conn = psycopg2.connect( host="localhost", user="postgres", password="mysecretpassword", dbname="postgres" )


# In[27]:


cur = conn.cursor()


# In[30]:


cur.execute( "SELECT count(*) FROM  shipment" )
for count in cur.fetchall() :
    print(count)


# In[31]:


conn.close()

