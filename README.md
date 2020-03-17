
<h1>Image to Text Converter</h1>


<h2>Introduction</h2>
<p>This is a simple app which extract textual data from a given image</p>

<h2>Structure</h2>

<ul>
    <li>This app structure consist of two tables(Images,Text_image)</li>
    <li>Image(which store image file)</li>
    <li>Image_text(which store textual data of image(oneToOne (Image)))</li>
    <li>Input:  Image file</li>
    <li>Output :Textual data of image</li>
</ul>


<h2>Installation</h2>
<ul>
    <li>install python</li>
    <li>install django</li>
    <li>install tesearact(python library)
            <li>mac:conda(or whatever virtual envoirnment your are using)</li>
            <li>windows:install binary file in your pc <a href="https://github.com/UB-Mannheim/tesseract/wiki">Link</a> Then add path to your views pytesseract.tesseract_cmd = '< your path of tesseract installer exe >'</li>
    </li>
    <li>Make migrations</li>
    <li>Url for adding images: 127.0.0.1:8000</li>
    <li>Url for getting  data from rest API: 127.0.0.1:8000/images</li>
    
    
</ul>
