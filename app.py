import streamlit as st

def rule_engine(data):
    errors = []
    if data['المسمى الوظيفي'] == 'مدير مشروع' and data['المؤهل'] in ['ثانوية عامة', 'دبلوم']:
        errors.append("تعارض: مدير مشروع لا يتوافق مع هذا المؤهل.")
    if data['العمر'] < 18:
        errors.append("العمر أقل من 18 غير مسموح.")
    return errors

def confidence_score(errors):
    if not errors:
        return 100
    return max(0, 100 - len(errors)*20)

st.set_page_config(page_title="رقيب", layout="centered")

st.title("رقيب - درع جودة البيانات")
st.subheader("النموذج الأولي")

name = st.text_input("الاسم")
degree = st.selectbox("المؤهل", ["ثانوية عامة", "دبلوم", "بكالوريوس", "ماجستير", "دكتوراه"])
job = st.selectbox("المسمى الوظيفي", ["موظف", "مشرف", "مدير مشروع", "محلل"])
age = st.number_input("العمر", 0, 100, 25)

if st.button("فحص البيانات"):
    entry = {
        'الاسم': name,
        'المؤهل': degree,
        'المسمى الوظيفي': job,
        'العمر': age
    }
    
    errors = rule_engine(entry)
    score = confidence_score(errors)
    
    st.divider()
    
    if errors:
        for e in errors:
            st.error(e)
    else:
        st.success("لا توجد أخطاء منطقية.")
    
    st.info(f"درجة الثقة: {score}%")
