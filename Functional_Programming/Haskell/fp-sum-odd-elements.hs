f :: [Int] -> Int
f = sum . filter odd

main :: IO ()
main = do
  inputdata <- getContents
  putStrLn $ show $ f $ map (read :: String -> Int) $ lines inputdata
