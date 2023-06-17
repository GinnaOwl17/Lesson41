#!/usr/bin/env python
# coding: utf-8

# **Асимптотическая сложность** - это способ подсчета необходимых вычислительных ресурсов(время, память) во время выполнения программы.
# Когда говорят об асимптотике, чаще всего имеют в виду Big O Notation (или O-большое). Оно позволяет описать наихудший из сценариев работы программы.

# In[7]:


# как не надо: много перебора! Асимптотическая сложность - О(N^2) => O(5^2) => O(25)
def strcount(s):
    for el in s:
        counter = 0
        for sub_el in s:
            if sub_el == el:
                counter += 1
        print(el, counter)
            
strcount('aabcd')


# In[2]:


# set - множество(оставляет только уникальные элементы)
print(set('abbcd'))


# In[5]:


# как сделать чуть лучше, имеет меньшую асимптотическую сложность - O(M*N) => O(4*5) = > О(20)
def strcount_plus(s):
    for el in set(s):
        counter = 0
        for sub_el in s:
            if sub_el == el:
                counter += 1
        print(el, counter)
            
strcount_plus('aabcd')


# In[6]:


# оптимальный вариант, асимптотическая сложность - O(M+N) => O(5+4) => O(9)
def strcount_pluss(s):
    el_counter = {}
    for el in s:
        el_counter[el] = el_counter.get(el, 0) + 1 # 5 операций
    for el, count in el_counter.items(): № # 4 операции
        print(el, count)
strcount_pluss('aabcd')


# In[ ]:





# In[ ]:





# In[ ]:




