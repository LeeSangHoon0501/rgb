import streamlit as st
import cv2
import numpy as np

st.set_page_config(
    page_title='인공지능이 보는 세상'
)

st.title(':computer: CCD가 보는 세상')
st.divider()

col1, col2, col3 = st.columns([2, 1, 2])
with col1:
    img_file_buffer = st.camera_input('웹캠 데이터')
with col2:
    st.write('OR')
with col3:
    upload_img = st.file_uploader('이미지파일을 업로드해주세요.')


def convert_rgb(img):
    bytes_data = img.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write('이미지의 데이터의 Shape:', cv2_img.shape)

    # RGB로 변환
    rgb_frame = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)

    # 각 채널로 분리
    r_channel, g_channel, b_channel = cv2.split(rgb_frame)
    
    # 색의 합성
    merged_r = cv2.merge([r_channel, np.zeros_like(r_channel), np.zeros_like(r_channel)])
    merged_g = cv2.merge([np.zeros_like(g_channel) , g_channel, np.zeros_like(g_channel)])
    merged_b = cv2.merge([np.zeros_like(b_channel), np.zeros_like(r_channel), b_channel])
    merged_rgb = cv2.merge([r_channel, g_channel, b_channel])
    merged_rg = cv2.merge([r_channel, g_channel, np.zeros_like(b_channel)])
    merged_gb = cv2.merge([np.zeros_like(r_channel), g_channel, b_channel])
    merged_rb = cv2.merge([r_channel, np.zeros_like(g_channel), b_channel])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Red')
        st.image(r_channel)
        st.write(r_channel.shape)

    with col2:
        st.write('Green')
        st.image(g_channel)
        st.write(g_channel.shape)

    with col3:
        st.write('Blue')
        st.image(b_channel)
        st.write(b_channel.shape)
    st.divider()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Red')
        st.write(r_channel)

    with col2:
        st.write('Green')
        st.write(g_channel)

    with col3:
        st.write('Blue')
        st.write(b_channel)
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('Red')
        st.image(merged_r)

    with col2:
        st.write('Green')
        st.image(merged_g)

    with col3:
        st.write('Blue')
        st.image(merged_b)
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write('R+G')
        st.image(merged_rg)

    with col2:
        st.write('G+B')
        st.image(merged_gb)

    with col3:
        st.write('R + B')
        st.image(merged_rb)
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col2:
        st.write('R + G + B')
        st.image(merged_rgb)


if img_file_buffer is not None:
    convert_rgb(img_file_buffer)

elif upload_img is not None:
    convert_rgb(upload_img)
    
