import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
import numpy as np
st.text("Test")

total_slurry_needed = 52
pump_out = 0.084
displacement_fluid = 112.8
displacing_mud = 11
old_mud = 10
toc = 3937
tvd = 5167
fc = 5078
od = 5.5
csd = 5156
#total_slurry_needed = st.session_state['total_slurry_need'] 
#pump_out = st.session_state['pump_out']
#displacement_fluid = st.session_state['displacement_fluid']
#displacing_mud = st.session_state['displacing_mud']
#old_mud = st.session_state['old_mud']
#toc = st.session_state['toc']
#tvd = st.session_state['tvd']
#fc = st.session_state['fc']
#od = st.session_state['od']
#csd = st.session_state['csd']

with st.container():
  st.title("CEMENTING - DETAILS")
  st.header("TOTAL VOLUME OF SLURRY NEEDED - "+str(total_slurry_needed))
  cement_den = st.number_input("CEMENT DENSITY (PPG) - ",min_value=1) 
  cementyld = st.number_input("CEMENT YIELD (CF-SK) - ",min_value=0.1)  
  cement_sk = (total_slurry_needed/(cementyld*0.178))         
  preflush = st.number_input("PRE-FLUSH VOL (bbls) - ",min_value=1)
  woc = st.number_input("PLANNED WOC (HRS)- ",min_value=1)
  st.header("CEMENT-RECEIPE")
  col1,col2,col3 = st.columns(3)
  with col1:
    name1 = st.text_input("RECEIPE NAME - ",key=1)
    name2 = st.text_input("RECEIPE NAME - ",key=2)
    name3 = st.text_input("RECEIPE NAME - ",key=3)
    name4 = st.text_input("RECEIPE NAME - ",key=4)
    name5 = st.text_input("RECEIPE NAME - ",key=5)
            
  with col2:
    bowc1 = st.number_input("BWOC PERCENTAGE - ",key=6)
    bowc2 = st.number_input("BWOC PERCENTAGE - ",key=7)
    bowc3 = st.number_input("BWOC PERCENTAGE - ",key=8)
    bowc4 = st.number_input("BWOC PERCENTAGE - ",key=9)
    bowc5 = st.number_input("BWOC PERCENTAGE - ",key=10)
         
  with col3:
    galsk1 = st.number_input("GAL/SACK - ",key=11)
    galsk2 = st.number_input("GAL/SACK - ",key=12)
    galsk3 = st.number_input("GAL/SACK - ",key=13)
    galsk4 = st.number_input("GAL/SACK - ",key=14)
    galsk5 = st.number_input("GAL/SACK - ",key=15)

df = pd.DataFrame()
df['receipe_name'] = [name1,name2,name3,name4,name5]
df['bwoc'] = [bowc1,bowc2,bowc3,bowc4,bowc5]
df['galsk'] = [galsk1,galsk2,galsk3,galsk4,galsk5]
try:           
  df['output-1'] = ((df['bwoc']/100)*94*cement_sk)
except:
  pass         
df['output-2'] = df['galsk']*cement_sk          
df['unit-1'] = np.where(df['output-1'] != 0 ,"Lbs","")     
df['unit-2'] = np.where(df['output-2'] != 0 ,"Gal","") 
df['output'] = df['output-1'] + df['output-2']           
df['unit'] =   df['unit-1'] + df['unit-2'] 
bt0 = st.button("SUBMIT")
bump_p =  ((toc*old_mud*0.052)+((tvd-toc)*cement_den*0.052)-((displacing_mud*fc*0.052)+((tvd-fc)*0.052*cement_den))+500)
if bt0:
  st.dataframe(df) 
  st.header("CEMENTING PROGRAM")
  st.write("LOWER "+str(od)+" CASING AND LAND SHOE @ "+str(csd)+"FT AND F/C @ "+str(fc)+"FT")
  st.write("M/UP CIRCULATING HEAD AND CIRCULATE AND CONDITION MUD PRIOR TO "+ str(od) +" CASING CEMENT JOB") 
  st.write("CARRY OUT PRE-JOB SAFETY MEETINGS.")
  st.write("PRESSURE TEST CEMENTING LINES @500 AND 2000 PSI")
  st.write("PRE MIX CEMENT AS PER RECEIPE AND PREPARE "+str(total_slurry_needed)+" OF CEMENT SLURRY ")
  preflush_stk = preflush/pump_out
  st.write("PUMP "+str(preflush)+" OF PRE FLUSH THROUGH RIG PUMP. "+"STROKES - "+str(preflush_stk))
  st.write("DROP BOTTOM PLUG.")
  st.write("MIX AND PUMP "+str(total_slurry_needed)+" OF "+str(cement_den)+" PPG SLURRY BY CEMENTING UNIT.")          
  st.write("DROP TOP PLUG")
  displace_stk = displacing_fluid/pump_out
  st.write("DISPLACE CEMENT WITH "+str(displacement_fluid)+" BBLS ("+str(displace_stk)+" STK) OF MUD TILL PLUG BUMPS. (BUMPING PRESSUE @ "+str(bump_p)+". PRESSURISE PLUG FURTHER TO 500 PSI)")
  st.write("BLEED OFF PRESSURE AND CHECK FOR BPV HOLDING")          
  st.write("WOC FOR "+str(woc)+" HRS TILL THE SURFACE CEMENT SETS")
