INSERT INTO auth.user (user_id, email, password, display_name, created, updated)
VALUES (uuid_generate_v4(), 'test@example.com', 'p', 'Test User', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);
