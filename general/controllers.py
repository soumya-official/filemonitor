from general.models import *
from general.serializers import *
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .script import *
import json
import pdb
from pprint import pprint


def get_general_info_list(request,table_name):
    try:

        folder_list = ['grep -rnw "/home/vinodreddy/folder1" -e "{}"','grep -rnw "/home/vinodreddy/folder2" -e "{}"']
        file_details= []
        for i in folder_list:

            start_exec([i.format(table_name)])
            
            general_info = get_platform(i.format(table_name))
            for j in general_info.split("\n"):
                if j!="":
                    file_details.append(j)

        return file_details
    except Exception as error:
        print(error)
