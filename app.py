import streamlit as st

st.set_page_config(page_title="課程回饋表單", page_icon="📋")

# 1. 頁面說明文字
st.title("課程回饋表單")
st.write(
    "感謝您參與本課程！這份表單用來收集您對課程的寶貴意見，"
    "請依照實際感受填寫，您的回饋將作為未來課程規劃與改進的重要參考。"
)
st.caption("填寫時間約 1 分鐘，所有回饋僅用於課程改善。")

# 2. 將科系選擇放到 Sidebar
st.sidebar.header("個人資料")
department = st.sidebar.selectbox(
    "科系",
    ["資訊工程系", "電子工程系", "其他"],
)

with st.form("feedback_form"):
    # 姓名
    name = st.text_input("姓名")

    # 課程滿意度 1~5 分
    satisfaction = st.radio(
        "課程滿意度（1~5 分）",
        [1, 2, 3, 4, 5],
        horizontal=True,
    )

    # 意見回饋
    comment = st.text_area("意見回饋")

    # 送出按鈕
    submitted = st.form_submit_button("送出")

# 送出後處理
if submitted:
    # 3. 姓名未填寫時顯示警告訊息
    if not name.strip():
        st.warning("請先填寫姓名再送出表單。")
    else:
        # 4. 成功送出後，顯示姓名、科系與滿意度
        st.success("感謝您的回饋！表單已成功送出。")
        st.write("### 您填寫的內容")
        st.write(f"**姓名：** {name}")
        st.write(f"**科系：** {department}")
        st.write(f"**課程滿意度：** {satisfaction} 分")
        if comment.strip():
            st.write(f"**意見回饋：** {comment}")
