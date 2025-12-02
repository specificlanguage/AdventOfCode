#IO.puts("Hello world from Elixir")

file = File.read!("day1input")
commands = String.split(file, "\n")

defmodule Day1 do

  def turn(direction, curr) do
    # Parse the number
    str_num = String.slice(direction, 1, 3)
    {count, _} = Integer.parse(str_num, 10)

    # Turn it
    dir = String.first(direction)
    case dir do
      "L" -> Integer.mod(curr - count, 100)
      "R" -> Integer.mod(curr + count, 100)
    end
  end

  def turn_rec([direction | tail], accumulator, num_zeros) do
    # IO.puts(direction <> " #{accumulator}" <> " #{num_zeros}")
    pos = turn(direction, accumulator)
    case pos do
      0 -> turn_rec(tail, pos, num_zeros + 1)
      _ -> turn_rec(tail, pos, num_zeros)
    end
  end

  def turn_rec([], _, num_zeros) do
    num_zeros
  end
end

ans = Day1.turn_rec(commands, 50, 0)
IO.puts(ans)