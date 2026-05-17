-- Write your query below

Select st.student_id, st.student_name 
from student as st 
where 
st.student_id in (select student_id from exam)
and
st.student_id not in (
    Select distinct student_id 
    from exam inner join (
        Select exam_id, max(score) as MaxScore, min(score) as MinScore 
        from exam 
        group by exam_id
    ) ex on exam.exam_id = ex.exam_id 
    where score = MaxScore or score = MinScore
)
order by st.student_id;