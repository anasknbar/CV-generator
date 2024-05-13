import os
import sys
import uuid
import re
my_list = [] # this list accumulate the data needed for the summary.

def main():
  
  generated_cv()
  summary_cv()

def generated_cv():
  welcome_message()
  arr = open_template()
  
  # each function return a list that combined them to 'combined_list'
  combined_list = personal_info(arr) + education(arr) + experience(arr) + skills(arr) + languages(arr)
  
  with open("assets/cv_output.txt",'a') as file:
    for line in combined_list:
      file.write(line)
  
def welcome_message():
  
  print("***************************************************************************************************************")
  print("*                                                                                                             *")
  print("                        \033[1;33mwlcome to GEN_CV a terminal CV generator that will make your life easy\033[0m")
  print("*                                                                                                             *")
  print("***************************************************************************************************************\n")

  print('you will be prompted with series of question for differnt CV parts.')
  user_input = input("type 'start' to procced: ").lower().strip()
  
  if user_input != 'start':
    sys.exit()
    
def open_template():
  
  current_dir = os.path.dirname(os.path.abspath(__file__))
  root_dir = os.path.dirname(current_dir)
  assets_folder = os.path.join(root_dir, 'assets')
  cv_template_path = os.path.join(assets_folder, 'cv_template.txt')
  
  try:
    with open(cv_template_path,'r') as file:
      content = list()
      lines = file.readlines()
      for line in lines:
        content.append(line)
      return content
  except FileNotFoundError:
    sys.exit("File Not Existed")
    
def personal_info(arr):
  personal_info_lines = arr[0:8]
  user_inputs = dict()
  
  print("\033[1;34m==[ Personal Information ]==========================================")       
  name = input("Name: ") # I need this for the summary
  my_list.append(name)
  user_inputs['Name'] = name 
  
  user_inputs['Phone Number'] = input("Phone Number: ")
  user_inputs['Email'] = input("Email: ")
  user_inputs['City'] = input("City: ")
  
    
  user_answer = list()
  for line in personal_info_lines:
    if "{Name}" in line:
      user_answer.append(line.replace('{Name}',user_inputs['Name']))
    elif '{phone_number}' in line:
      user_answer.append(line.replace('{phone_number}',user_inputs['Phone Number']))
    elif '{email}' in line:
      user_answer.append(line.replace('{email}',user_inputs['Email']))
    elif '{city}' in line:
      user_answer.append(line.replace('{city}',user_inputs['City']))
    else:
      user_answer.append(line)
  
  return user_answer
  
def education(arr):
  education_lines = arr[8:15]
  user_inputs = dict()
  print("\033[1;32m==[ Education ]=====================================================")       
  
  user_inputs['University Name'] = input("University Name: ")
  major =input("Major in: ") # I need this for the summary
  my_list.append(major)
  user_inputs['Major in'] = major
  
  user_inputs['Graduation Date'] = input("Graduation Date: ")
  
  user_answer = list()
  for line in education_lines:
    if "{university_name}" in line:
      user_answer.append(line.replace('{university_name}',user_inputs['University Name']))
    elif '{major}' in line:
      user_answer.append(line.replace('{major}',user_inputs['Major in']))
    elif '{graduation_date}' in line:
      user_answer.append(line.replace('{graduation_date}',user_inputs['Graduation Date']))
    else:
      user_answer.append(line)
      
  return user_answer

def experience(arr):
  experience_lines = arr[15:23]
  
  user_inputs = dict()
  print("\033[1;94m==[ Experience ]=====================================================")       
  
  company = input("Company Name: ") # I need this for the summary
  my_list.append(company)
  user_inputs['Company Name'] = company 
  
  job = input("Job Title: ") # I need this for the summary
  my_list.insert(2,job)
  user_inputs['Job Title']=job
  user_inputs['responsibilities'] = input("Summary of your key responsibilities: ")
  
  user_answer = list()
  for line in experience_lines:
    if "{company_name}" in line:
      user_answer.append(line.replace('{company_name}',user_inputs['Company Name']))
    elif '{job_title}' in line:
      user_answer.append(line.replace('{job_title}',user_inputs['Job Title']))
    elif '{you responsibilities}' in line:
      user_answer.append(line.replace('{you responsibilities}',user_inputs['responsibilities']))
    else:
      user_answer.append(line)
  
  return user_answer
  
def skills(arr):
  skills_lines = arr[23:31]
  
  user_inputs = dict()
  print("\033[1;36m==[ Skills ]=====================================================")       
  
  user_inputs['skill-01'] = input("skill-01: ")
  user_inputs['skill-02'] = input("skill-02: ")
  user_inputs['skill-03'] = input("skill-03: ")
  user_inputs['skill-04'] = input("skill-04: ")
  
  user_answer = list()
  for line in skills_lines:
    if "{skill-01}" in line:
      user_answer.append(line.replace('{skill-01}',user_inputs['skill-01']))
    elif '{skill-02}' in line:
      user_answer.append(line.replace('{skill-02}',user_inputs['skill-02']))
    elif '{skill-03}' in line:
      user_answer.append(line.replace('{skill-03}',user_inputs['skill-03']))
    elif '{skill-04}' in line:
      user_answer.append(line.replace('{skill-04}',user_inputs['skill-04']))
    else:
      user_answer.append(line)
  
  return user_answer
  
def languages(arr):
  languages_lines = arr[31:41]
  
  user_inputs = dict()
  
  print("\033[1;33;33m==[ Languages ]=====================================================")         
  user_inputs['Arabic'] = input("Arabic_level: ")
  user_inputs['English'] = input("English_level: ")
 
  
  user_answer = list()
  for line in languages_lines:
    if "{Arabic_language_level}" in line:
      user_answer.append(line.replace('{Arabic_language_level}',user_inputs['Arabic']))
    elif '{English_language_level}' in line:
      user_answer.append(line.replace('{English_language_level}',user_inputs['English']))
    else:
      user_answer.append(line)
  
  return user_answer 

# required test_functions
def read_template(path):
  try:
    with open(path,'r') as file:
      lines = file.readline()
      return(lines)
  except IOError:
    raise IOError('file not existed')
# required test_functions
def parse_template(string):
  mathces = re.search(r"^.*\{(.*)\}.*\{(.*)\}.*\{(.*)\}.*\{(.*)\}.*$",string)
  if mathces:
    name,major,job,company = mathces.groups()
  new_str = re.sub(r"\{.*?\}","{}",string)
  print(new_str)
  return new_str,(name,major,job,company)
# required test_functions
def merge(text,arr):
  name,major,job,company = arr
  new_str = str()
  for index,word in enumerate(arr):
    if index == 0:
      new_str = re.sub(r"\{.*?\}",arr[index],text,count=1)
    else:
      new_str = re.sub(r"\{.*?\}",arr[index],new_str,count=1)
  return new_str


def summary_cv():
  with open("assets/personal_summary_template.txt",'r') as file:
    
    text = file.readline()
    with open("assets/summary.txt",'w') as file:
      file.write(merge(text,my_list))
      
      
      
  
 
 
if __name__ == '__main__':
  main()