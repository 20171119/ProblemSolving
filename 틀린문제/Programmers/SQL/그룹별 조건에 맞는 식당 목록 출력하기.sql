# max 회원의 이름, 리뷰, 날짜 찾기

select x.MEMBER_NAME, y.REVIEW_TEXT, date_format(y.REVIEW_DATE, "%Y-%m-%d") review_date
from member_profile x inner join rest_review y
on x.member_id = y.member_id
where (y.member_id) in 
    -- ------------------ max 회원 찾기
    (select member_id
    from rest_review
    group by member_id
    having count(member_id) =
        -- -------------------- max 찾기
        (select max(cnt)
        from (
        select count(member_id) cnt
        from rest_review
        group by member_id) a
        )
        -- --------------------
    )
    -- ------------------
order by review_date
-- --------