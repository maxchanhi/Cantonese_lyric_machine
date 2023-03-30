#def solfege_song(dict_tone):
    #dict_tone = dict_tone.replace(' ', '')
    #result = [solfege[int(t)-1] if int(t)-1 < len(solfege) else "" for t in dict_tone]
    #return result
def figue_song(dict_tone):
    tone = [3,9,4,0,5,2,7,8,6] 
    dict_tone = dict_tone.replace(' ', '')
    result = [tone[int(t)-1] if int(t)-1 < len(tone) else "" for t in dict_tone]
    return result
css = '''
<style>
    .button {
        display: inline-block;
        background-color: #faf898;
        color: white;
        text-align: center;
        padding: 5px 10px;
        border-radius: 10px;
        text-decoration: none;
        cursor: pointer;
    }
    .button:hover {
        background-color: yellow;
    }
</style>
'''