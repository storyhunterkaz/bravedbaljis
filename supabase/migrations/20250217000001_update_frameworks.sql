-- Update the profiles table to use the correct BRAVED and BALAJIS frameworks
ALTER TABLE profiles
  DROP COLUMN braved_scores,
  DROP COLUMN balajis_scores;

ALTER TABLE profiles
  ADD COLUMN braved_scores JSONB DEFAULT '{
    "bitcoin": 0,
    "real_world": 0,
    "ai": 0,
    "vrar": 0,
    "emotional": 0,
    "decentralization": 0
  }',
  ADD COLUMN balajis_scores JSONB DEFAULT '{
    "build": 0,
    "attention": 0,
    "leverage": 0,
    "algorithms": 0,
    "joy": 0,
    "influence": 0,
    "skills": 0
  }'; 