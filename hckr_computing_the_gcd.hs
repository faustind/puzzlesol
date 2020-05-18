
_gcd :: Integral a => a -> a -> a
_gcd m n 
  | n == 0 = m 
  | otherwise = gcd n (m `mod` n)


gcd' :: Integral a => a -> a -> a
gcd' m n
  | n > m = _gcd n m
  | otherwise = _gcd m n

main :: IO ()
main = do
    [a, b] <-fmap (\[a, b]->(a,b)) . map (read::String->Int) . words
    print $ gcd' a b
