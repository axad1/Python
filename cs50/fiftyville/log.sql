-- description of the crime scene report
SELECT * FROM crime_scene_reports
WHERE day = 28 AND month = 7 AND street = "Humphrey Street";
-- interview transcript
SELECT * FROM interviews
WHERE day = 28 AND month = 7 AND transcript LIKE "%bakery%";

-- 10 minutes in parking of bakery_security_logs
SELECT * FROM bakery_security_logs
WHERE day = 28 AND month = 7 AND hour = 10 AND minute >= 15 AND minute <= 25 AND activity = "exit";
-- names of people in that exits from parking
SELECT * FROM people
WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
        WHERE day=28 AND month=7 AND hour=10 AND minute>=15 AND minute<=25 AND activity="exit");

-- ATM withdraw at Leggett Street
SELECT * FROM atm_transactions
WHERE day = 28 AND month = 7 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";
-- names of people that make withdraw
SELECT * FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
        WHERE day=28 AND month=7 AND transaction_type = "withdraw" AND atm_location = "Leggett Street";

-- called for less than a minute
SELECT * FROM phone_calls
WHERE day = 28 AND month = 7 AND duration < 60;
-- names of caller
SELECT * FROM people
    JOIN phone_calls ON phone_number = caller
        WHERE day=28 AND month=7 AND duration<60;
-- name of receivers
SELECT * FROM people
    JOIN phone_calls ON phone_number = receiver
    WHERE day=28 AND month=7 AND duration<60;

-- earliest flight next day
SELECT * FROM flights
WHERE day = 29 AND month = 7
ORDER BY hour, minute
LIMIT 1;
-- name of accomplice who took earliest flight ticket
SELECT * FROM people
    JOIN passengers ON people.passport_number = passengers.passport_number
    JOIN flights ON passengers.flight_id = flights.id
        WHERE day=29 AND month=7
        ORDER BY hour, minute
        LIMIT 1;

-- destination
SELECT * FROM airports
    JOIN flights ON airports.id = flights.destination_airport_id
        WHERE day=29 AND month=7
        ORDER BY hour, minute
        LIMIT 1;
        

select name from people join passengers on people.passport_number = passengers.passport_number
where flight_id = (select id from flights where day=29 and month=7 order by hour limit 1)
intersect
SELECT name FROM people
    JOIN phone_calls ON phone_number = caller
        WHERE day=28 AND month=7 AND duration<60
intersect
SELECT name FROM people
    JOIN bank_accounts ON people.id = bank_accounts.person_id
    JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
        WHERE day=28 AND month=7 AND transaction_type = "withdraw" AND atm_location = "Leggett Street"
    intersect
    SELECT name FROM people
WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
        WHERE day=28 AND month=7 AND hour=10 AND minute>=15 AND minute<=25 AND activity="exit");