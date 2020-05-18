
nextr :: [Int] -> [Int]
nextr xs = zipWith (+) (0:xs) (xs++[0])

pascal :: [[Int]]
pascal = iterate nextr [1] 

showPascal :: Int -> String
-- A string representation of the first k lines of the pascal triangle
showPascal k
  = unlines $ map (unwords . map show) (take k pascal)

main :: IO ()
main = do
    k <- readLn::IO Int
    putStr $ showPascal k
