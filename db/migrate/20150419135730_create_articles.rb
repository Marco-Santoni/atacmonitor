class CreateArrivals < ActiveRecord::Migration
  def change
    create_table :arrivals do |t|
      t.string :line, null: false
      t.integer :minutes
      t.timestamp :created_at, null: false
    end
  end
end
