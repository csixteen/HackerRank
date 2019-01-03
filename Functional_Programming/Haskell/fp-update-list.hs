f :: [Int] -> [Int]
f = map abs

main :: IO ()
main = do
  inputdata <- getContents
  mapM_ putStrLn $ map show $ f $ map (read :: String -> Int) $ lines inputdata

