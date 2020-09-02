import streamlit as st
import streamlit.components.v1 as stc
from pathlib import Path
import base64


def get_table_download_link():
    with open("resources/Resume.pdf", "rb") as pdf_file:
        b64 = base64.b64encode(pdf_file.read()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a class="btn btn-dark" role="button" href="data:file/Resume.pdf;base64,{b64}" download="AnmolChawlaResume.pdf">Download Resume</a>'
    return href

def write():
    curr_dir = Path.cwd()
    st.title("About Me")
    st.image("resources/anmol.jpg", width=700, height=900)
    st.markdown(get_table_download_link(), unsafe_allow_html=True)

    footer_temp = """
    	 <!-- CSS  -->
    	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
    	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
    	 <footer class="page-footer grey darken-4">
    	    <div class="container" id="aboutapp">
    	      <div class="row">
    	        <div class="col l6 s12">
    	          <h5 class="white-text">Anmol Chawla's Online Portfolio</h5>
    	          <p class="grey-text text-lighten-4">Open to collabortions and new opportunities</p>
    	        </div>

    	   <div class="col l3 s12">
    	          <h5 class="white-text">Connect With Me</h5>
    	          <ul>
    	            <a href="https://www.instagram.com/anmol_chawla_himself/" target="_blank" class="white-text">
    	            <i class="fab fa-instagram fa-4x"></i>
    	          </a>
    	          <a href="https://www.linkedin.com/in/chawla-anmol" target="_blank" class="white-text">
    	            <i class="fab fa-linkedin fa-4x"></i>
    	          </a>
    	          <a href="https://www.youtube.com/watch?v=Bx4o4ySijSo&t=608s" target="_blank" class="white-text">
    	            <i class="fab fa-youtube-square fa-4x"></i>
    	          </a>
    	           <a href="https://github.com/anmolchawla" target="_blank" class="white-text">
    	            <i class="fab fa-github-square fa-4x"></i>
    	          </a>
    	          </ul>
    	        </div>
    	      </div>
    	    </div>
    	    </div>
    	  </footer>
    	"""
    stc.html(footer_temp, height = 500)