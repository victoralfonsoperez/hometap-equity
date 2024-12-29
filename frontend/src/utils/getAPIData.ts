import axios from 'axios'

export type API_response = {source_1: [
  {
    bathrooms: number
    bedrooms: number
    lotSizeSqFt: number
    propertyType: string
    roomCount: number
    salePrice: number
    septicSystem: boolean
    squareFootage: number
    yearBuilt: number
  }
], source_2: [{
    bathrooms: number
    bedrooms: number
    lotSizeSqFt: number
    propertyType: string
    roomCount: number
    salePrice: number
    septicSystem: boolean
    squareFootage: number
    yearBuilt: number
}]}

export async function getAPIData (queryParams: string) {
  let response
  let loading: boolean
  loading = true
  try {
    const {data} = await axios.get<API_response>(`${"http://localhost:8000/home_equity"}?search_query=${queryParams}`)
    response = data
  } catch (err) {
    // here we can use a logging service to log the error on the app
    console.error(err)
  } finally {
    loading = false
  }
  
  return {response, loading}
}