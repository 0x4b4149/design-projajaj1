import streamlit as st

st.set_page_config(page_title="課程回饋表單", page_icon="📋")

st.title("課程回饋表單")
st.write("請填寫以下表單，感謝您的參與！")

with st.form("feedback_form"):
    # 1. 姓名
    name = st.text_input("姓名")

    # 2. 科系
    department = st.selectbox(
        "科系",
        ["資訊工程系", "電子工程系", "其他"],
    )

    # 3. 課程滿意度 1~5 分
    satisfaction = st.radio(
        "課程滿意度（1~5 分）",
        [1, 2, 3, 4, 5],
        horizontal=True,
    )

    # 4. 意見回饋
    comment = st.text_area("意見回饋")

    # 5. 送出按鈕
    submitted = st.form_submit_button("送出")

# 6. 按下送出後顯示訊息
if submitted:
    st.success("感謝您的回饋！")
    st.write("### 您填寫的內容")
    st.write(f"**姓名：** {name}")
    st.write(f"**科系：** {department}")
    st.write(f"**課程滿意度：** {satisfaction} 分")
    st.write(f"**意見回饋：** {comment}")
