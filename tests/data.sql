INSERT INTO users (username, hash)
VALUES
  ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
  ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO recipe (title, instructions, chef_id, ingredients, preparation_time, difficulty, Category)
VALUES
  ('test title', 'test' || x'0a' || 'body', 1, 'test igredients', 1, 'test difficulty', 'test category');
