#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
def is_stressful(subj):
    return (subj.isupper() or
            subj.endswith('!!!') or
            any(re.search('+[.!-]*'.join(word), subj.lower())
            for word in ['help', 'asap', 'urgent']))

