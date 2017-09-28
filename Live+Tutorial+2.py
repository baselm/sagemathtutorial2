
# coding: utf-8

# In[1]:

g1 = Graph({'a':['b', 'f'], 'b':['f','e','c'],'f':['a','e'],'d':[]}); g1


# In[4]:

g1.neighbors('b')


# In[3]:

g1.degree('a')


# In[5]:

g1.adjacency_matrix()


# In[6]:

g1.incidence_matrix()


# In[14]:

d1 = DiGraph({'a':['a'], 'b':['a','c'], 'c':['d'], 'd':['b','a','c']}); d1


# In[20]:

def toprint(l):
    print "The Degree is a: ",
    print l.degree('a')
    print "The Neighbors are: ",
    print l.neighbors('b')
    print "The adjacency_matrix: " 
    print l.adjacency_matrix()
    print "The incidence_matrix: "
    print l.incidence_matrix()
    return;


# In[22]:

g2 = Graph({'a':['a','b','b','b','e'], 'b':['e','d','c'], 'c':['c','d','d','d'],'d':['e']}, multiedges=True); g2


# In[21]:

toprint(d1)


# In[25]:

def handshak(h):
    sumofdegree=0
    for v in h.vertices():
        sumofdegree = sumofdegree + h.degree(v)
    print sumofdegree 
    print 2* h.num_edges()
    if sumofdegree == 2* h.num_edges():
        return "2m = sum of the degree of each vertix"
    else:
        return "handshaking theorem is not true"


# In[27]:

handshak(d1)

