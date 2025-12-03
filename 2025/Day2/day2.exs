file = File.read!("day2input")
ranges = String.split(file, ",")
# Wow look at these awesome maps and data manip
ranges = Enum.map(ranges, fn range ->
  List.to_tuple(Enum.map(String.split(range, "-"), fn x -> String.to_integer(x) end))
end)

defmodule Day2 do

  # Actually does the check
#  def sublist2(digits, check) do
#    num_copies = trunc(length(digits)/ length(check))
#    compare_list = List.flatten(List.duplicate(check, num_copies))
#    compare_list == digits
#  end

  # Checks through all possible prefixes
#  def is_invalid(digits, check) when length(check) > length(digits) do false end
#  def is_invalid(digits, check) do
#    [head | rest] = digits
#    if rem(length(digits), length(check)) != 0 do is_invalid(rest, check ++ [head]) end
#    case sublist(digits, check) do
#      true -> true
#      false -> is_invalid(rest, check ++ [head])
#    end
#  end

  # Just the helper for a single number
  def is_invalid_rec(num) when num < 11 do 0 end
  def is_invalid_rec(num) do
    digits = Integer.digits(num)
#    [head | _] = digits
#    res = is_invalid(digits, [head])
#    IO.puts("#{res} #{num}")
#    case is_invalid(digits, [head]) do
    split_list = Enum.chunk_every(digits, trunc(length(digits) / 2))
    case split_list do
      [h1 | [h2 | []]] ->
        case h1 == h2 do
          true -> num
          false -> 0
        end
      _ -> 0
    end
  end

  # This does one range
  def count_nums_helper(rstart, rend) do
    Enum.reduce(rstart..rend, 0, fn x, acc -> acc + is_invalid_rec(x) end)
  end

  def count_ranges(ranges) do
    Enum.reduce(ranges, 0, fn {rstart, rend}, acc -> acc + count_nums_helper(rstart, rend) end)
  end
end

#IO.puts(Day2.is_invalid_rec(2))
#IO.puts(Day2.count_nums_helper(11, 22))
IO.puts(Day2.count_ranges(ranges))