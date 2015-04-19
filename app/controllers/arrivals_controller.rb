class ArrivalsController < ApplicationController

  def index
    @arrivals = Arrival.all
  end

end
