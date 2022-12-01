from Spider import Spider
import requests # request img from web
import shutil # save img locally
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
from urllib.parse import urljoin, urlparse
import os



URL = 'https://www.shirikasacco.co.ke/wp-content/uploads'
#spider = Spider(URL)

def Get(URL):
	r = requests.get(URL)
	Content = BeautifulSoup(r.content,'html.parser')

	return Content

def extract_folder_links(url,URL):
	
	Content = Get(url)
	image_URL = []
	count = 0
	for i,img in enumerate(tqdm(Content.find_all("a"), "Extracting images")):
		count+=1
		img_url = img.attrs.get("href")
		if not img_url:
		# if img does not contain src attribute, just skip
			pass


		else:
			img_url = urljoin(URL, img_url)
			image_URL.append(img_url)

	return image_URL


def download_image(url, pathname):
    """
    Downloads a file given an URL and puts it in the folder `pathname`
    """

    # download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    # get the total file size
    file_size = int(response.headers.get("Content-Length", 0))
    # get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    # progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    if os.path.isfile(pathname):
    	print('File already exists')
    	return None
    if not os.path.isfile(pathname):
	    progress = tqdm(response.iter_content(1024), f"Downloading {pathname}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)
	    with open(pathname, "wb") as f:
	        for data in progress.iterable:
	            # write data read to the file
	            f.write(data)
	            # update the progress bar manually
	            progress.update(len(data))






def iterate_links(URL):
	ls =extract_folder_links(URL,URL)
	print(URL)
	Path1 = 'UPLOADS'
	make_dir(Path1)
	if len(ls) != 0:
		#Main directory
		count = 0
		path_rst0 = Path1
		for i in ls:
			Path = path_rst0
			count+=1
			name = i.split("/")[-1].strip()
			print(name)

			if  count>3:
				i = i.rstrip('/')
				print(Path)
				
				Path = os.path.join(Path, i.split("/")[-1])
				print(i.split("/")[-1])
				print(Path)
				print(i)

				if i.find("jpg")!= -1 or i.find("png")!= -1 :
					download_image(i,Path)

				else:
					ls1 = extract_folder_links(i,URL)
					make_dir(Path)
					
					if len(ls1) != 0:
						count1 = 0
						Path_rst1 = Path
						for j in ls1:
							j = j.rstrip('/')
							count1+=1
							Path = Path_rst1

							if count1>3:

								Path = os.path.join(Path, j.split("/")[-1])
								print(j)
								print(Path)

								if j.find("jpg")!= -1 or j.find("png")!= -1:
									download_image(j,Path)

								else:
									ls2 = extract_folder_links(j,URL)
									make_dir(Path)

									if len(ls2) != 0:
										count2 = 0
										Path_rst2 = Path
										for k in ls2:
											k = k.rstrip('/')
											Path = Path_rst2
											count2+=1
											if count2>3:

												Path = Path.rstrip('/')
												Path = os.path.join(Path, k.split("/")[-1])
												
												if k.find("jpg")!= -1 or k.find("png")!= -1 :
													download_image(k,Path)
													print(Path)

												elif k.find("jpg")== -1 or k.find("png")== -1 :
													make_dir(Path)
													continue


	else:
		print('URL list empty')




def test():

	i = 'www.shirikasacco.co.ke/wp-content/uploads/2013/'
	print(i)

	print(i.split("/")[-1])




def make_dir(name):
	print('MAKING DIRECTORY , ',name)
	try:
		if not os.path.isdir(name):
			os.makedirs(name,exist_ok=True)
	except:
		print('Could Not Create Directory')

iterate_links(URL)