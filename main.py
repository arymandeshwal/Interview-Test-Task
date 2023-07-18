#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Importing modules
from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd


# In[11]:


#SPARQL endpoint
endpoint_url = "https://dbpedia.org/sparql"


# In[12]:


# Writing query for SPARQL, gathering subjects and labels in english
query = """
SELECT ?s ?label
WHERE{

    {
        ?s a dbo:ChemicalSubstance .
    }
    UNION
    {
        ?s a dul:ChemicalObject .
    }
    UNION
    {
        ?s a umbel-rc:ChemicalSubstanceType .
    }
    UNION
    {
        ?s a yago:Chemical114806838 .
    }
    UNION
    {
        ?s a yago:Compound105870180 .
    }
    UNION
    {
        ?s a yago:Substance100019613 .
    }
    UNION
    {
        ?s a yago:Matter100020827 .
    }
    UNION
    {
        ?s a yago:Part113809207 .
    }
    UNION
    {
        ?s a yago:Mixture114586258 .
    }
    UNION
    {
        ?s gold:hypernym dbr:Element .
    }
    UNION
    {
        ?s a yago:Alloy114586769 .
    }
   
    OPTIONAL {
        ?s rdfs:label ?label .
        FILTER (lang(?label) = 'en')
    }
    
    FILTER (
        NOT EXISTS { ?s a yago:Abstraction100002137 . }
    )
    
    FILTER (BOUND(?label))
    
}
"""


# In[13]:


#Executing the query
sparql = SPARQLWrapper(endpoint_url)
sparql.setQuery(query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()['results']['bindings']


# In[14]:


#Creating a nested list with the output of query, so that it can be used to create a dataframe.
data = []
for res in results:
    data.append([res['s']['value'],res['label']['value']])


# In[15]:


#Creating a dataframe
df = pd.DataFrame(data, columns=["DBpediaURI","EnglishLabel"])


# In[16]:


#rows and columns in our df
print(df.shape)


# In[17]:


#Top 5 rows of our df
print(df.head())


# In[18]:


#Saving the df to output.tsv
df.to_csv('output.tsv', sep='\t', index=False)


# In[ ]:




