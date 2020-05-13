import Control.Monad


main :: IO ()
main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    forM_ [1..n] $ \boh  -> do
        q_temp <- getLine
        let q = read q_temp :: Int
        rawInput <- getMultipleLines q
        let input = [(read (words str !! 0) :: Int, read (words str !! 1) :: Int ) | str <- rawInput]
        -- here starts your code


getMultipleLines :: Int -> IO [String]
getMultipleLines n
    | n <= 0 = return []
    | otherwise = do          
        x <- getLine         
        xs <- getMultipleLines (n-1)    
        let ret = (x:xs)    
        return ret
