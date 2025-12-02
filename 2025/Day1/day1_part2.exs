#IO.puts("Hello world from Elixir")

# Parse the entry file
file = File.read!("day1input")
commands = String.split(file, "\n")

defmodule Day1 do

  # Right is counting up here

  def turn(direction, start) do
    # Parse the number
    str_num = String.slice(direction, 1, 5)
    {count, _} = Integer.parse(str_num)

    # Calculate new position
    dir = String.first(direction)

    pos = case dir do
      "L" -> start - count
      "R" -> start + count
    end

    IO.puts("#{pos}")
    new_pos = Integer.mod(pos, 100)
    clicks = abs(Integer.floor_div(pos, 100))
    case {dir, start, new_pos} do
      {"L", 0, 0} -> {new_pos, clicks}
      {"L", 0, _} -> {new_pos, max(clicks - 1, 0)}
      {"L", _, 0} -> {new_pos, max(clicks + 1, 0)}
      _ -> {new_pos, clicks}
    end
    # Left from 0 to 0 -> no change
    # Right from 0 to 0 -> no change
    # Left from 0 to non-zero -> need -1 click
    # Right from 0 to non-zero -> no change
    # Left from non-zero to 0 -> need +1 click
    # Right from non-zero to 0 -> no change
  end

  def turn_rec([], _, num_zeros) do num_zeros end
  def turn_rec([direction | tail], accumulator, num_zeros) do
    IO.puts(direction <> " #{accumulator}" <> " #{num_zeros}")
    {pos, clicks} = turn(direction, accumulator)
    turn_rec(tail, pos, num_zeros + clicks)
  end
end

ans = Day1.turn_rec(commands, 50, 0)
IO.puts(ans)