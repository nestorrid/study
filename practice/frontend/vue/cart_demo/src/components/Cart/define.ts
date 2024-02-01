export interface Product {
    id: number,
    name: string,
    desc: string,
    price: number,
    curprice: number,
    sold: number,
    score: number,
    inventory: number,
    image: string,
    count?: number,
}

export interface Category {
    id: number,
    name: string,
    isActive?: boolean
}