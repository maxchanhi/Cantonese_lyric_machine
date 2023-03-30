import streamlit as st
from function import *
st.title("Cantonese Intonation and Melody Helper")
solfege = ['l', 'f-s', 'f', 'r-d', 'm-f', 'r', 'l', 'f', 'r']
columns = st.columns(len(solfege))

# Place an input box inside each column
st.write("Customise solfege of each tone:")
for i in range(len(solfege)):
    syllable = columns[i].text_input(f"{i+1}", solfege[i])
    solfege[i] = syllable.strip() 

dict_tone = st.text_input("Enter the tone from dictionary of each word (e.g. 6 1 5 1 3 6 1):")
def solfege_song(dict_tone):
    dict_tone = dict_tone.replace(' ', '')
    result = [solfege[int(t)-1] if int(t)-1 < len(solfege) else "" for t in dict_tone]
    return result
if dict_tone:
    song = solfege_song(dict_tone)
    st.write("Solfege notes:", ", ".join(song))
with open("helper.html", "r") as f:
    html_code = f.read()
st.markdown(html_code, unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.write("When setting lyrics to melody, the interval of each tone is not absolute. However, it is important to maintain the order of the phonemic tones from low to high when setting musical pitches to the tone. Since pitches 1 and 7, 3 and 8, and 6 and 9 are the same, respectively, within the same musical phrase, make sure they are on the same musical pitch.")
with col2:
    st.image("Untitled.png","credit: cantonese.ca")
st.markdown("""The solfège I created is subjective. The actual pronunciation of these tones may vary in practice. For example, the medium rising tone (2) may be glided higher than the first tone at the end, and the low tone (4) is sometimes not glided downward. To better distinguish between tones, the starts of tones 2, 4, 5, and 6 are set to different pitches, adding more melodic characteristics when singing.""")
st.markdown(css, unsafe_allow_html=True)
st.markdown('<a href="https://www.instagram.com/maxchanhi/" target="_blank"><div class="button">Created by @maxchanhi</div></a>', unsafe_allow_html=True)
