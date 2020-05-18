-- HackerRank: Compute the area of a polygon

import Control.Monad

area :: [(Double, Double)] -> Double
area poly = (xy - yx) / 2
    where poly' = poly ++ [head poly] 
          xs = map fst poly'
          ys = map snd poly'
          xy = sum (zipWith (*) (init xs) (tail ys))
          yx = sum (zipWith (*) (tail xs) (init ys))

main :: IO ()
main = do
    n <- readLn :: IO Int
    poly <- forM [1..n] 
            (\_ -> fmap ((\[a, b]->(a,b)) . map (read::String->Double) . words) getLine :: IO (Double, Double))
    print $ area poly
