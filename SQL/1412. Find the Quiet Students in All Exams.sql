select student_id, student_name 
from student,
    (select distinct aa.stud 
        from
            
     (select exam.student_id stud
            from    exam, 
      
                    (select exam.exam_id c_examid, student_id c_stuid, a.mins m_scr 
                     from exam,
                     (select exam_id, min(score) mins
                        from exam
                        group by exam_id) a 
                     where a.exam_id = exam.exam_id and exam.score = a.mins) c,

                    (select exam.exam_id d_examid, student_id d_stuid, b.maxs mx_scr 
                    from exam,
                    (select exam_id,max(score) maxs
                        from exam
                        group by exam_id) b 
                    where b.exam_id = exam.exam_id and exam.score = b.maxs) d

            where c.c_examid = exam.exam_id and d.d_examid = exam.exam_id and exam.score > c.m_scr and exam.score < d.mx_scr) aa
     
    where aa.stud not in (select student_id c_stuid from exam,(select exam_id, min(score) mins
    from exam
        group by exam_id) a where a.exam_id = exam.exam_id and exam.score = a.mins) and 
        aa.stud not in (select student_id d_stuid from exam,(select exam_id,max(score) maxs
    from exam
        group by exam_id) b 
                        
    where b.exam_id = exam.exam_id and exam.score = b.maxs)) final
    
where final.stud = student.student_id

