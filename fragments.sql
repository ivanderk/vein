-- Insert sample users. Both have password 'hola' 
INSERT INTO "user" (id, login, name, email, password_hash, password_salt)
VALUES (1, 'john', 'John Singleton','jsingleton@justacorp.com','$2b$12$gIcSbXQrWqMHTFhbcNOguOQhSNDDq.nQpuX25Fgfy4HKrrIScnaWm', '$2b$12$gIcSbXQrWqMHTFhbcNOguO'),
       (2, 'jane', 'Jane Mutiplex','jmutiplex2@justacorp.com','$2b$12$NRjQ1na2/7ikf2SFhgqNrOE8cUQOI.JiFWy8WUQepghNZEPmbAT/m', '$2b$12$NRjQ1na2/7ikf2SFhgqNrO');

-- Insert sample Projects. 
INSERT INTO "project" (id, name)
VALUES (1, 'Presales team'),
       (2, 'CoE Cloud Google'),
       (3, 'Project Crew Verve');

-- Associate projects with users
INSERT INTO user_project (user_id, project_id)
VALUES (1, 1),
       (1, 2),
       (2, 2),
       (2, 3);

-- create Survey for projects
INSERT INTO survey (id, title,closed, project_id )
VALUES (1, "CoE Google - febrero 2023", false, 2);

-- create Ticket for survey
INSERT into ticket (id, completed, user_id, survey_id)
VALUES (1, false, 1, 1)

