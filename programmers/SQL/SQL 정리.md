[TOC]



## SQL 정리

---

### 조건문 - 아닌 경우 조회

- !=, <>

  ```sql
  SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
  WHERE INTAKE_CONDITION != 'Aged'
  ORDER BY ANIMAL_ID ASC
  ```

- NOT IN

  ```sql
  SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
  WHERE INTAKE_CONDITION NOT IN ('Aged')
  ORDER BY ANIMAL_ID ASC
  ```

- NOT

  ```sql
  SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
  WHERE NOT INTAKE_CONDITION = 'Aged'
  ORDER BY ANIMAL_ID ASC
  ```

- 차이점

  - 조건을 하나만 명시할 경우 != 사용 추천
  - 조건을 여러 개 명시할 경우 OR을 사용하는데 비교가 선형적이라 많아질 수록 효율이 떨어짐
  - 조건이 많을 때는 IN 사용, IN에 명시한 값들을 정렬하고 이진 탐색으로 찾기 때문에 효율이 좋다
  - 가독성 측면에서도 IN을 사용하는 것을 추천



---

### LIMIT

- 가장 맨 위 행 N개만 조회할 떄 LIMIT 구문 사용

  ```sql
  SELECT NAME
  FROM ANIMAL_INS
  ORDER BY DATETIME
  LIMIT 1
  ```



---

### GROUP BY  절

- SELECT 문에서 GROUP BY 절을 사용하는 경우 디비는 쿼리 된 테이블의 행을 그룹으로 묶는다.
- 디비는 선택 목록의 집계 함수를 각 행 그룹에 적용하고 각 그룹에 대해 단일 결과 행을 반환한다.
- GROUP BY 절을 생략하면 디비는 선택 목록의 집계 함수를 쿼리 된 테이블의 모든 행에 적용합니다.
- SELECT절의 모든 요소는 GROUP BY 절의 표현식, 집계 함수를 포함하는 표현식 또는 상수만 가능.
- **GROUP BY로 SELECT한 값에 대해 조건을 걸 때는 HAVING, 조건을 걸고 GROUP BY할 것이라면 WHERE**

![image-20230215104605624](SQL 정리.assets\image-20230215104605624.png)

```sql
SELECT USER_ID, PRODUCT_ID FROM ONLINE_SALE GROUP BY USER_ID, PRODUCT_ID HAVING COUNT(*) >= 2 ORDER BY USER_ID, PRODUCT_ID DESC
```

```sql
SELECT A.INGREDIENT_TYPE, SUM(B.TOTAL_ORDER) AS TOTAL_ORDER FROM ICECREAM_INFO A, FIRST_HALF B WHERE A.FLAVOR = B.FLAVOR GROUP BY A.INGREDIENT_TYPE ORDER BY TOTAL_ORDER
```

```sql
SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS FROM CAR_RENTAL_COMPANY_CAR 
WHERE OPTIONS LIKE '%열선시트%' OR OPTIONS LIKE '%통풍시트%' OR OPTIONS LIKE '%가죽시트%'
GROUP BY CAR_TYPE 
ORDER BY CAR_TYPE ASC
```

```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS 'count' FROM ANIMAL_INS GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE ASC
```

```SQL
# HAVING 절에서 이름이 NULL이면 COUNT되지 않음
SELECT NAME, COUNT(NAME) AS 'COUNT' FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME
SELECT NAME, COUNT(ANIMAL_ID) AS 'COUNT' FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(NAME) > 1 ORDER BY NAME

# HAVING 절에서 이름이 NULL인 값은 제외하지 못함
SELECT NAME, COUNT(ANIMAL_ID) AS 'COUNT' FROM ANIMAL_INS GROUP BY NAME HAVING COUNT(ANIMAL_ID) > 1 ORDER BY NAME
```

```SQL
SELECT HOUR(DATETIME) AS 'HOUR' , COUNT(ANIMAL_ID) AS 'COUNT' FROM ANIMAL_OUTS WHERE HOUR(DATETIME) >= 9 AND HOUR(DATETIME) < 20 GROUP BY HOUR(DATETIME) ORDER BY HOUR(DATETIME)
```

```SQL
SELECT FLOOR(PRICE/10000)*10000 AS PRICE_GROUP, COUNT(PRODUCT_ID) AS PRODUCT FROM PRODUCT GROUP BY PRICE_GROUP ORDER BY PRICE_GROUP

SELECT  CASE WHEN (0 < PRICE) AND (PRICE < 10000) then 0
             WHEN (10000 <= PRICE) and (PRICE < 20000) then 10000
             WHEN (20000 <= PRICE) and (PRICE < 30000) then 20000
             WHEN (30000 <= PRICE) and (PRICE < 40000) then 30000
             WHEN (40000 <= PRICE) and (PRICE < 50000) then 40000
             WHEN (50000 <= PRICE) and (PRICE < 60000) then 50000
             WHEN (60000 <= PRICE) and (PRICE < 70000) then 60000
             WHEN (70000 <= PRICE) and (PRICE < 80000) then 70000
             WHEN (80000 <= PRICE) and (PRICE < 90000) then 80000
             END AS PRICE_GROUP, count(*)
  FROM  PRODUCT 
 GROUP 
    BY  PRICE_GROUP
 ORDER
    BY  PRICE_GROUP
```



---

### JOIN

- 둘 이상의 테이블에서 데이터가 필요한 경우 테이블 조인이 필요
- 일반적으로 조인 조건을 포함하는 WHERE 절을 작성해야 함
- 조인 조건은 일반적으로 각 테이블의 PK 및 FK로 구성됨
- JOIN의 종류
  - INNER JOIN
  - OUTER JOIN
    - LEFT OUTER JOIN
    - RIGHT OUTER JOIN
- JOIN 조건의 명시에 따른 구분
  - NATURAL JOIN
  - CROSS JOIN(FULL JOIN, CARTESIAN JOIN)
- 주의
  - 조인의 처리는 어느 테이블을 먼저 읽을지를 결정하는 것이 중요 (처리할 작업량이 상당히 달라짐)
  - INNER JOIN
    - 어느 테이블을 먼저 읽어도 결과가 달라지지 않아 MySQL 옵티마이저가 조인의 순서를 조절해서 다양한 방법으로 최적화를 수행할 수 있음
  - OUTER JOIN
    - 반드시 OUTER가 되는 테이블을 먼저 읽어야 하므로 옵티마이저가 조인 순서를 선택할 수 없

```sql
SELECT BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME, DATE_FORMAT(BOOK.PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE FROM BOOK 
JOIN AUTHOR ON BOOK.AUTHOR_ID = AUTHOR.AUTHOR_ID 
WHERE BOOK.CATEGORY = '경제' 
ORDER BY PUBLISHED_DATE
```

```SQL
SELECT PRODUCT.PRODUCT_CODE, SUM(PRODUCT.PRICE * OFFLINE_SALE.SALES_AMOUNT) AS SALES 
FROM PRODUCT 
JOIN OFFLINE_SALE ON PRODUCT.PRODUCT_ID = OFFLINE_SALE.PRODUCT_ID 
GROUP BY PRODUCT.PRODUCT_ID
ORDER BY SALES
```

```SQL
SELECT PRODUCT.PRODUCT_CODE, SUM(OFFLINE_SALE.SALES_AMOUNT) * PRODUCT.PRICE AS SALES 
FROM PRODUCT 
JOIN OFFLINE_SALE ON OFFLINE_SALE.PRODUCT_ID = PRODUCT.PRODUCT_ID 
GROUP BY OFFLINE_SALE.PRODUCT_ID
ORDER BY SALES DESC, PRODUCT_CODE
```





---

### Subquery

- 서브 쿼리(Subquery)란 다른 쿼리 내부에 포함되어 있는 SELECT 문을 의미
- 서브 쿼리를 포함하고 있는 쿼리를 외부 쿼리(outer query)또는 메인 쿼리라고 부르며, 서브 쿼리는 내부 쿼리(inner query)라고 부름
- 서브 쿼리는 비교 연산자의 오른쪽에 기술해야하고 반드시 괄호로 감싸져 있어야 함
- 서브 쿼리의 종류
  - 중첩 서브 쿼리(Nested Subquery)
    - WHERE 문에 작성하는 서브 쿼리
      - 단일 행
      - 복수(다중) 행
      - 다중 컬럼
    - 인라인 뷰(Inline View)
      - FROM 문에 작성하는 서브 쿼리
    - 스칼라 서브 쿼리(Scalar Subquery)
      - SELECT 문에 작성하는 서브 쿼리
- 주의
  - 서브쿼리는 반드시 괄호로 감싸야 함
  - 서브 쿼리는 단일 행 또는 다중 행 비교 연산자와 함께 사용됨
- 서브 쿼리가 사용 가능한 곳
  - SELECT
  - FROM
  - WHERE
  - HAVING
  - ORDER BY
  - INSERT문의 VALUES
  - UPDATE문의 SET
- 
