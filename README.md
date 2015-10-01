# UBHD-OMPPortal
UBHD-OMPPortal is a flexible, responsive Frontend portal for [pkp's](https://pkp.sfu.ca/) [Open Monograph Press](https://pkp.sfu.ca/omp/) and [Open Journal Systems](https://pkp.sfu.ca/ojs/) written in python programming language and  based on the python web framework [web2py](http://www.web2py.com).

# Demo
- Heidelberg University Publishing  [Web](http://heiup.uni-heidelberg.de/)
- Customized HTML Viewer [Full book](http://heiup.uni-heidelberg.de/reader/index/43/heiUP_habenstein_abwesenheit_2015.xml) ,  [Chapter ](http://heiup.uni-heidelberg.de/reader/index/43/43-69-209-1-10-20150717.xml) ,  [Chapter with images](http://heiup.uni-heidelberg.de/reader/index/43/43-69-220-1-10-20150723.xml#figures)
![alt tag](static/images/UBHD-OMPPortal.png)

# Features
- Responsive design (based on twitter bootstrap)
- Easy multilingual support
- Intergrated-HTML viewer (based on [lens](https://github.com/elifesciences/lens/))
- Native [JATS](http://jats.nlm.nih.gov/) XML support for OMP
- Chapter level metadata for monographs and edited volumes
- Social sharing  (without using external plugins)
- Detailed usage statistics
- Easy migration using web2py app structure

# Installation
- Prerequisites
    1. Install Open Monograph Press. See [documentation](http://pkp.sfu.ca/omp/README)
    2. Install web2py
     1. [Download] (http://web2py.com/init/default/download) web2py
     2. Unzip it
     3. run ```python2.7 web2py.py```
- Install UBHD-OMPPortal
     1. ```cd  **web2py_folder**/applications/```
     2. ```git clone https://github.com/UB-Heidelberg/UBHD-OMPPortal.git **press_name**```
       - Notice:  **press_name** *should* contain only characters, numbers or _
       - Please do not use **-** in the **press_name**
     3. Change the settings for your local omp installation private/appconfig.ini
       1. **username** and **password** for the OMP database
       2. **press_id** of the local omp press
       3. define the **press_name**
     4. mount or link the files folder of the OMP  to **web2py_folder**/applications/**press_name**/static/monographs/

       ```
        ln -s web2py_folder/applications/press_name/static/monographs/ omp_folder/files/presses/press_id/monographs
        ```


# For developers
##General information
- A general knowledge in python  and sql is necessary for further development.
- Some  basic knowledge in web2y is helpful. See [docs](http://web2py.com)
- The OJS intergration is work in progress.
- We have included a minified [lens](https://github.com/elifesciences/lens/) viewer. If you want to customize it, either use the [lens git](https://github.com/elifesciences/lens/)  or  [contact us](mailto:dulip.withanage@gmail.com). We will be happy to help you.

##Folder structure
**strictly follows MVC (Model-View-Control) design principle**

- **controllers** - contains all the functions for  enabling pages.
- **cron** - automated tasks
- **languages** -  language files. Web2py generates automatic entries for any word written as {{=T('my-word')}}. Default language is english.
- **models** - database models for Open monograph press. Web2py uses a  data abstraction layer.
- **private** - all the files, which contain sensitive information and configuration files
- **modules** - define your own modules, to be imported to your application
- **static** - all the static files as such as javascript files and css files.
- **views** - for each controller file, you have to  add a folder  with the same name and a html file for each function in the controller file.

#License
This software is released under the the [GNU General Public License](LICENSE.md).
See the file [LICENSE.md](LICENSE.md) included with this distribution for the terms of this license.











