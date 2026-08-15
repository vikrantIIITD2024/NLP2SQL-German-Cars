# Database Dictionary
# semantic layer:
## dimensions

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### length_mm
- Type: INTEGER
- Semantic: numeric
- Description: Length mm.

### width_mm
- Type: INTEGER
- Semantic: numeric
- Description: Width mm.

### height_mm
- Type: INTEGER
- Semantic: numeric
- Description: Height mm.

### wheelbase_mm
- Type: INTEGER
- Semantic: numeric
- Description: Wheelbase mm.

### boot_space_litres
- Type: INTEGER
- Semantic: numeric
- Description: Boot space litres.

## engine_configuration

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### engine_type
- Type: TEXT
- Semantic: engine
- Description: Engine type.

### displacement_cc
- Type: INTEGER
- Semantic: numeric
- Description: Displacement cc.

### cylinders
- Type: INTEGER
- Semantic: numeric
- Description: Cylinders.

### transmission_type
- Type: TEXT
- Semantic: transmission
- Description: Transmission type.

### drivetrain
- Type: TEXT
- Semantic: drivetrain
- Description: Drivetrain.

## master_overview

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### variant_trim
- Type: TEXT
- Semantic: categorical
- Description: Variant trim.

### body_type
- Type: TEXT
- Semantic: body_type
- Description: Body type.

### launch_year
- Type: INTEGER
- Semantic: year
- Description: Launch year.

### segment
- Type: TEXT
- Semantic: market_segment
- Description: Segment.

## power_performance

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### power_ps
- Type: INTEGER
- Semantic: performance
- Unit: PS
- Description: Maximum engine output measured in metric horsepower. Time required to accelerate from 0 to 100 km/h. Maximum certified vehicle speed.

### torque_nm
- Type: INTEGER
- Semantic: performance
- Unit: Nm
- Description: Torque nm.

### accel_0_100_sec
- Type: REAL
- Semantic: performance
- Unit: seconds
- Description: Accel 0 100 sec.

### top_speed_kmh
- Type: INTEGER
- Semantic: numeric
- Description: Top speed kmh.

### fuel_efficiency_kmpl
- Type: REAL
- Semantic: fuel_economy
- Unit: km/l
- Description: Average certified fuel efficiency measured in kilometres per litre.

## price

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### ex_showroom_min_inr_lakh
- Type: REAL
- Semantic: numeric
- Description: Ex showroom min inr lakh.

### ex_showroom_max_inr_lakh
- Type: REAL
- Semantic: numeric
- Description: Ex showroom max inr lakh.

### top_variant_price_inr_lakh
- Type: REAL
- Semantic: price
- Unit: INR lakh
- Description: Top variant price inr lakh.

### currency
- Type: TEXT
- Semantic: categorical
- Description: Currency.

### price_as_of_date
- Type: TEXT
- Semantic: price
- Description: Price as of date.

## ratings_reviews

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### expert_rating_out_of_10
- Type: REAL
- Semantic: rating
- Description: Expert rating out of 10.

### user_rating_out_of_5
- Type: REAL
- Semantic: rating
- Description: User rating out of 5.

### review_count
- Type: INTEGER
- Semantic: numeric
- Description: Review count.

## safety

### car_id
- Type: TEXT
- Semantic: categorical
- Description: Car id.

### brand
- Type: TEXT
- Semantic: manufacturer
- Description: Brand.

### model
- Type: TEXT
- Semantic: vehicle_model
- Description: Model.

### ncap_rating_stars
- Type: INTEGER
- Semantic: rating
- Description: Ncap rating stars.

### ncap_body
- Type: TEXT
- Semantic: categorical
- Description: Ncap body.

### airbags_count
- Type: INTEGER
- Semantic: numeric
- Description: Airbags count.

### adas_available
- Type: TEXT
- Semantic: categorical
- Description: Adas available.

### abs_esc_available
- Type: TEXT
- Semantic: categorical
- Description: Abs esc available.

