-- Actual infinity as a first-class value; existence-by-observation.
-- Run: runghc haskell_actual_infinity.hs

module Main where

-- An infinite object defined by self-reference. This is a fractal
-- held whole in the hand: the definition IS the limit of its unrollings.
fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-- All the primes, as a completed totality (Berkeleyan idealism:
-- each exists exactly insofar as it is observed/forced).
primes :: [Integer]
primes = sieve [2..]
  where sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p /= 0]

-- A stream that never ends, zipped against one that does:
-- the infinite is TAMED BY THE FINITE observer.
labeled :: [(Int, Integer)]
labeled = zip [1..] primes

main :: IO ()
main = do
  putStrLn $ "fibs (first 12):   " ++ show (take 12 fibs)
  putStrLn $ "primes (first 10): " ++ show (take 10 primes)
  putStrLn $ "1000th prime:      " ++ show (primes !! 999)
  putStrLn ""
  putStrLn "`fibs` and `primes` are ACTUAL infinite values -- passed to"
  putStrLn "functions, stored, shared. Yet only the observed prefix ever"
  putStrLn "exists in memory. Esse est percipi, enforced by the runtime."
