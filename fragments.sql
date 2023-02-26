-- Insert sample users. Both have password 'hola' 
INSERT INTO "user" (id, login, name, email, password_hash, password_salt)
VALUES (1, 'john', 'John Singleton','jsingleton@justacorp.com','$2b$12$gIcSbXQrWqMHTFhbcNOguOQhSNDDq.nQpuX25Fgfy4HKrrIScnaWm', '$2b$12$gIcSbXQrWqMHTFhbcNOguO'),
       (2, 'jane', 'Jane Mutiplex','jmutiplex2@justacorp.com','$2b$12$NRjQ1na2/7ikf2SFhgqNrOE8cUQOI.JiFWy8WUQepghNZEPmbAT/m', '$2b$12$NRjQ1na2/7ikf2SFhgqNrO');

-- Insert sample Projects. 
INSERT INTO "project" (id, name)
VALUES (1, 'Presales team'),
       (2, 'CoE Cloud Google'),
       (3, 'Project Crew Verve');


-- -- Insert sample projects
-- INSERT INTO project (id, name)
-- VALUES (1, 'Asociación de vecinos'),
--        (2, 'Club de deporte'),
--        (3, 'Pilates club');

-- -- Associate projects with users
-- INSERT INTO user_project (user_id, project_id)
-- VALUES (1, 1),
--        (1, 2),
--        (2, 2),
--        (2, 3);

-- -- Insert sample tasks
-- INSERT INTO task (id, name, complete, project_id)
-- VALUES (1, 'Reconstruir piscina', false, 1),
--        (2, 'Limpieza de aparcamiento', true, 1),
--        (3, 'Event Madrid Agosto 2023', false, 2),
--        (4, 'Publicidad por Instragram', false, 2),
--        (5, 'Cambiar sala', true, 3);

-- -- Get all projects with tasks for a particular user

-- SELECT p.name AS project_name, t.name AS task_name, t.complete
-- FROM "user" u
-- JOIN user_project up ON u.id = up.user_id
-- JOIN project p ON up.project_id = p.id
-- JOIN task t ON p.id = t.project_id
-- WHERE u.name = 'john'