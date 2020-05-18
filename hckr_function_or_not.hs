-- HackerRank `Functions or Not?`

import Control.Monad
import Data.List (sort)



isFunction :: [(Int, Int)] -> Bool
isFunction = decide . sort 
    where
        decide xys = all (\((a,b), (c,d)) -> (a == c && b == d) || a /= c)
                         (zip (head xys:xys) (xys++[last xys]))

main :: IO ()
main = do
    t <- readLn::IO Int 
    forM_ [1..t] (\_ -> do
        n <- readLn::IO Int
        func <- forM [1..n] 
                (\_ -> fmap ((\[a, b]->(a,b)) . map (read::String->Int) . words) getLine :: IO (Int, Int)
                )
        putStrLn $ if isFunction func then "YES" else "NO")
