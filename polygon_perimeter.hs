-- HackerRank: Compute the perimeter of a polygon

import Control.Monad

distance :: (Floating a, Num a) => (a, a) -> (a, a) -> a
distance (a,b) (c,d) = sqrt $ (a-c)**2 + (b-d)**2

perimeter :: (Floating a, Num a) => [(a, a)] -> a
perimeter xs = sum ( zipWith distance (init xs) (tail xs)) + distance  (head xs) (last xs) 


main :: IO ()
main = do
    n <- readLn :: IO Int
    poly <- forM [1..n] 
            (\_ -> fmap ((\[a, b]->(a,b)) . map (read::String->Double) . words) getLine :: IO (Double, Double))
    print $ perimeter poly
